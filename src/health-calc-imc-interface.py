from __future__ import annotations


##IMC Numerical Categories Definition
 
CAT_UNDERWEIGHT_RANGE = 18.5

CAT_NORMAL_RANGE_BOTTOM = 18.5
CAT_NORMAL_RANGE_TOP = 25

CAT_PRE_OBESITY_BOTTOM= 25
CAT_PRE_OBESITY_TOP= 30

CAT_OBESITY_LEVEL1_BOTTOM= 30
CAT_OBESITY_LEVEL1_TOP= 35

CAT_OBESITY_LEVEL2_BOTTOM= 35
CAT_OBESITY_LEVEL2_TOP= 40

CAT_OBESITY_LEVEL3_BOTTOM= 40





class ImcCalculatorInterface:

    def __init__(self) -> None:
        pass


    def ImcCalculator(self, Weight:float, Height:float ) -> float:
        input_is_valid= self.ValidateInput(Weight, Height)
        if input_is_valid:
            result = Weight/( Height ** 2)
            print(result)
            return result
        else:
            raise Exception
    
    def ValidateInput():
        return True
        

    def GetImcCategory(self,imc:float) -> str:
        
        if imc < CAT_UNDERWEIGHT_RANGE:
            return "Abaixo do peso"
        elif imc> CAT_NORMAL_RANGE_BOTTOM and imc <= CAT_NORMAL_RANGE_TOP:
            return "Peso Normal"
        elif imc > CAT_PRE_OBESITY_BOTTOM and imc <= CAT_PRE_OBESITY_TOP:
            return "Pré-Obesidade"
        elif imc > CAT_OBESITY_LEVEL1_BOTTOM and imc <= CAT_OBESITY_LEVEL1_TOP:
            return "Obesidade Grau 1"
        elif imc > CAT_OBESITY_LEVEL2_BOTTOM and imc <= CAT_OBESITY_LEVEL2_TOP:
            return "Obesidade Grau 2"
        elif imc > CAT_OBESITY_LEVEL3_BOTTOM:
            return "Obesidade Grau 3"

 