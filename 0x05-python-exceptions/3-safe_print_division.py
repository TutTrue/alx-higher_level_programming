def safe_print_division(a, b):
    try:
        result = a / b
        print("Inside result: {:.1f}".format(result))
    except:
        result = None
        print("Inside result: None")
    finally:
        return result

