from othello_python import controller
from othello_python import model

if __name__ == "__main__":
    ctrl = controller.Controller(model.Color.WHITE)
    ctrl.start()
