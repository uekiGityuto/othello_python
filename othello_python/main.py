from controllers import controller
from models import model

if __name__ == "__main__":
    ctrl = controller.Controller(model.Color.WHITE)
    ctrl.start()
