from reporter.reporter import Reporter

class Console_reporter(Reporter):

    @staticmethod
    def report(dict):
        print(f"Report. \n Items count {len(dict)}")
        for key in dict.keys():
            print(key, dict[key])