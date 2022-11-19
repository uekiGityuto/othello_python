from othello_python import controller, model

if __name__ == "__main__":
    ctrl = controller.Controller(model.Color.WHITE)
    ctrl.start()
