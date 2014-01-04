try:
    None.some_method_none_does_not_know_about()
except Exception as ex:
    print ex.args[0]
