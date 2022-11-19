import controllers.controller as controller
import models.model as model

if __name__ == "__main__":
    ctrl = controller.Controller(model.Color.WHITE)
    ctrl.start()
