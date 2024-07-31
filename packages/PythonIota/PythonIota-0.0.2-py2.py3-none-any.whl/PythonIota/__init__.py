import re


def is_expression(s):
    pattern = r'^[\d+iota\s+\-*/()]+$'
    return True if re.match(pattern, s) else False


class Iota:
    def __init__(self, initial=0):
        self.current = initial
        self.values = {}

    def __call__(self, **kwargs):
        for key, value in kwargs.items():
            if value == "iota":
                self.values[key] = 0
                self.current = 1

            elif value == '':
                self.values[key] = self.current
                self.current += 1

            elif value == "_":
                self.current += 1

            elif value.isdigit():
                self.values[key] = int(value)
                self.current = self.values[key]+1


            elif is_expression(value):
                if "iota" in value:
                    value = value.replace("iota", str(self.current))
                    self.values[key] = eval(value)
                    self.current = self.values[key] + 1
                else:
                    self.values[key] = eval(value)
                    self.current = self.values[key] + 1

            elif len(value) == 1 and value.isalpha():
                # 如果值是单个字母，则赋值为上一个值加1
                self.values[key] = self.values[list(kwargs.keys())[-2]] + 1
            else:
                raise ValueError("Invalid value for iota assignment.")
            setattr(self, key, self.values[key])

    def __parseInput__(self,input_str):
        lines = input_str.strip().split("\n")
        args = {}
        for line in lines:
            if '=' in line:
                key, value = line.split('=',1)
                key = key.strip()
                value = value.strip()
            else:
                key = line.strip()
                value = ''
            args[key] = value
        self(**args)

    def get_values(self):
        return self.values



#iota_instance(AA="iota", BB="2*3", _="_", ZZ="99", CC="(iota+1)*2", DD="")
#print(iota_instance.get_values())



