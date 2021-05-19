class Pycharm:
    def compile(self):
        print("pycharm compiling")
    def execute(self):
        print("pycharm execute")
class Vscode:
    def compile(self):
        print("vsc compiling")
    def execute(self):
        print("vsc executing")
class programmer:
    def coding(self,ide):
        ide.compile()
        ide.execute()
p1=programmer()
py=Pycharm()
p1.coding(py)