# Import the nodes from which the following classes will inherit
from ...Node import *
from ...NodesVariables import *
from ...NodesOperations import *
from ...NodesDifferentiation import *
from ..BackendHelper import *

# Import backend specific packages
import aadc
import numpy as np
import scipy.stats
import scipy.special

###
### PyAadc specific nodes.
###

class VariableNodeAadc(VariableNode):
    def __init__(self, value, identifier=None):
        super().__init__(value, identifier)
        self.value = aadc.idouble(self.value)
        self.require_grad = True
        #self.value = self.value

    def Run(self):
        return self.value

class ConstantNodeAadc(ConstantNode):
    def Run(self):
        return aadc.idouble(self.value)
    def __str__(self):
        return f"constant({str(self.value)})"

class ExpNodeAadc(ExpNode):
    def Run(self):
        return np.exp(self.operand.Run())
    
class SinNodeAadc(SinNode):
    def Run(self):
        return np.sin(self.operand.Run())
    
class CosNodeAadc(SinNode):
    def Run(self):
        return np.cos(self.operand.Run())
    
class LogNodeAadc(LogNode):
    def Run(self):
        return np.log(self.operand.Run())
    
class SqrtNodeAadc(SqrtNode):
    def Run(self):
        return np.sqrt(self.operand.Run())
    
class PowNodeAadc(PowNode):
    def Run(self):
        return self.left.Run() ** self.right.Run()
    
class CdfNodeAadc(CdfNode):
    def Run(self):
        return scipy.stats.norm.cdf(self.operand.Run())
    
class ErfNodeAadc(ErfNode):
    def Run(self):
        return scipy.special.erf(self.operand.Run())

class ErfinvNodeAadc(ErfinvNode):
    def Run(self):
        return scipy.special.erfinv(self.operand.Run())

class MaxNodeAadc(MaxNode):
    def Run(self):
        return np.maximum(self.left.Run(), self.right.Run())

class RandomVariableNodeAadc(RandomVariableNode):
    def NewSample(self, sampleSize = 1):
        self.value = np.random.uniform(size = sampleSize)

class RandomVariableNodeAadcNormal(RandomVariableNode):
    def NewSample(self, sampleSize = 1):
        self.value = np.random.normal(size = sampleSize)

class SumNodeVectorizedAadc(Node):
    def __init__(self, operand):
        super().__init__()
        self.operand = self.ensure_node(operand)
        self.parents = [self.operand]
    def __str__(self):
        return f"sumVectorized({str(self.operand)})"
    def Run(self):
        return np.sum(self.operand.Run())
    def get_inputs(self):
        return self.operand.get_inputs()
    def get_inputs_with_diff(self):
        return self.operand.get_inputs_with_diff()
    def get_input_variables(self):
        return self.operand.get_input_variables()

class IfNodeAadc(IfNode):
        def Run(self):
            condition_value = self.condition.Run()
            true_value = self.true_value.Run()
            false_value = self.false_value.Run()
            return aadc.iif(condition_value, true_value, false_value)
##
## Differentiation node is created on the graph when .grad() is called for on a node
##
class DifferentiationNodeAadc(DifferentiationNode):
    def __init__(self, operand, diffDirection):
        super().__init__(operand, diffDirection)
        
    def backend_specific_grad(self):

        input_variables = self.get_inputs()
        #print(input_variables)
        input_dict = {var.identifier: var.value for var in input_variables}

        myfunc = self.operand.get_optimized_executable(input_dict, input_dict)
        
        result_class = ResultNodeAadc(self)
        
        _, gradient = result_class.eval_and_grad_of_function(myfunc, input_dict, input_dict)
        
        #_, gradient = self.eval_and_grad_of_function(myfunc, input_dict, input_dict)

        if isinstance(self.diffDirection, list):
            gradients = {}
            for direction in self.diffDirection:
                if isinstance(direction, VariableNodeAadc):
                    gradient_key = direction.identifier
                else:
                    gradient_key = direction
                
                if gradient_key not in gradient:
                    raise ValueError(f"Gradient for '{gradient_key}' not found in the computed gradients.")
                
                gradients[gradient_key] = gradient[gradient_key]
            gradients_as_array = list(gradients.values())
            return gradients_as_array
        else:
            # Handle the case where diffDirection is not a list
            if isinstance(self.diffDirection, VariableNodeAadc):
                gradient_key = self.diffDirection.identifier
            else:
                gradient_key = self.diffDirection
            
            if gradient_key not in gradient:
                raise ValueError(f"Gradient for '{gradient_key}' not found in the computed gradients.")
           
            return gradient[gradient_key]

##
## Result node is used within performance testing. It contains the logic to create optimized executables and eval/grad of these.
##
class ResultNodeAadc(ResultNode):
    def __init__(self, operationNode):
        super().__init__(operationNode)
    def eval(self):
        # #result
        # #print('fail here')
        # return self.operationNode.Run()
        input_variables = self.operationNode.get_inputs()
        #print(input_variables)
        input_dict = {var.identifier: var.value for var in input_variables}

        myfunc = self.operationNode.get_optimized_executable(input_dict, input_dict)
        
        result_class = ResultNodeAadc(self)
        
        result, gradient = result_class.eval_and_grad_of_function(myfunc, input_dict, input_dict)
        return result
    
    
    def eval_and_grad_of_function(self, myfunc, input_dict, diff_dict):
        return myfunc(input_dict)

    def create_optimized_executable(self, initial_input_dict, diff_dict): # For AADC input_dict and diff_dict are needed to create kernel through forward_pass
        expression = str(self.operationNode)
        function_mappings = self.get_function_mappings()
        for key, value in function_mappings.items():
            expression = expression.replace(key, value)
        input_names = self.operationNode.get_input_variables()
        numpy_func = BackendHelper.create_function_from_expression(expression, input_names,  {'aadc': aadc, 'np': np})

        ###
        ### Create AADC kernel for numpy_func that is evaluated in eval_and_grad_of_function(self, myfunc, input_dict, diff_dict)
        ###
                # Here we try to add aadc logic. myfunc is the func of the graph with inputs: input_dict and wanted derivatives diff_dict
        funcs = aadc.Functions()
        
        #keys_array = list(input_dict.keys())
        values_array = list(initial_input_dict.values())

        valuesAadc = []
        aadcArgs = []

        funcs.start_recording()

        for input_value in values_array:
            if isinstance(input_value, np.ndarray):
                value = aadc.idouble(input_value[0])
                valuesAadc.append(value)
                aadcArgs.append(value.mark_as_input_no_diff())
            else:
                value = input_value
                valuesAadc.append(value)
                aadcArgs.append(value.mark_as_input())

        index = 0
        aadc_input_dict = {}
        for key in initial_input_dict:
            aadc_input_dict[key] = valuesAadc[index]
            index += 1

        # Evaluate func with aadc idoubles
        result_optimized = numpy_func (**aadc_input_dict)

        fRes = result_optimized.mark_as_output()

        funcs.stop_recording()
        

        # def aadc_kernel_func(input_dict):
        #     #print(input_dict)
        #     values_array = input_dict.values()#list(input_dict.values())
        #     #print(values_array)
        #     # Create input dictionary for the aadc.evaluate
        #     inputs = {}
        #     for aadc_arg, value_entry in zip(aadcArgs, values_array):
        #         inputs[aadc_arg] = value_entry

        #     request = {fRes: [arg for arg in aadcArgs]}
            
        #     Res = aadc.evaluate(funcs, request, inputs, aadc.ThreadPool(4))
            
        #     aadc_eval_result = Res[0][fRes]
            
        #     gradient_dict = {}
        #     for aadc_arg, input_key in zip(aadcArgs, input_dict):
        #         gradient_dict[input_key] = np.sum(Res[1][fRes][aadc_arg])#currently only one-dimensional output
            
            # return np.sum(aadc_eval_result), gradient_dict

        def aadc_kernel_func(input_dict):
            values_array = input_dict.values()
            inputs = {aadc_arg: value_entry for aadc_arg, value_entry in zip(aadcArgs, values_array)}
            
            request = {fRes: aadcArgs}  
            
            Res = aadc.evaluate(funcs, request, inputs, aadc.ThreadPool(4))
            
            aadc_eval_result = Res[0][fRes]
            gradient_dict = {input_key: np.sum(Res[1][fRes][aadc_arg]) for aadc_arg, input_key in zip(aadcArgs, input_dict)}
            return np.sum(aadc_eval_result), gradient_dict
        
        
        #print(initial_input_dict)
        test, test2 = aadc_kernel_func(initial_input_dict)
        #print(test)
        #print(test2)
        
        return  aadc_kernel_func #numpy_func 
    
