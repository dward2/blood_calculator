def interface():
    print("Blood Analysis Program")
    while True:
        print("")
        print("Options for you")
        print("1 - HDL")
        print("2 - LDL")
        print("3 - Total Cholesterol")
        print("9 - Quit")
        choice = input("Enter your choice: ")
        if choice == '9':
            return
        elif choice == '1':
            HDL_driver()
        elif choice == '2':
            LDL_driver()
        elif choice == '3':
            total_driver()
            
def HDL_driver():
   # Get input
   HDL_result = get_test_result_input("HDL")
   # Check if HDL is normal
   HDL_analysis = analyze_HDL_result(HDL_result)
   # Output
   output_test_analysis("HDL", HDL_result, HDL_analysis)
   
def get_test_result_input(test_name):
    test_result = input(f"Enter the {test_name} result: ")
    return int(test_result)
    
def output_test_analysis(test_name, test_result, analysis):
    print("The {} result is {}".format(test_name, test_result))
    print("That is {}".format(analysis))
    
    
def analyze_HDL_result(HDL_test_value):
    if HDL_test_value >= 60:
        return "Normal"
    elif 40 <= HDL_test_value < 60:
        return "Borderline Low"
    else:
        return "Low"

def LDL_driver():
    LDL_result = get_test_result_input("LDL")
    LDL_analysis = analyze_LDL_result(LDL_result)
    output_test_analysis("LDL", LDL_result, LDL_analysis)
            
def analyze_LDL_result(LDL_test_value):
    if LDL_test_value < 130:
        return "Normal"
    elif 130 <= LDL_test_value < 160:
        return "Borderline high"
    elif 160 <= LDL_test_value < 190:
        return "High"
    else:
        return "Very high"

def total_driver():
    total_result = get_test_result_input("Total Cholesterol")
    total_analysis = analyze_total_result(total_result)
    output_test_analysis("Total Cholesterol", total_result, total_analysis)
    
def analyze_total_result(total_test_value):
    if total_test_value < 200:
        return "Normal"
    elif 200 <= total_test_value < 240:
        return "Borderline high"
    else:
        return "High"


interface()

