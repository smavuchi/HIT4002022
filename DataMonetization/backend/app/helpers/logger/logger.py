from timeit import default_timer as timer

class Logger(object):
  step_depth = 0
  step_factor = 3
  start_time = []

  def print(self, output):
    print(output)

  def step(self, message):
    self.print((" " * Logger.step_depth) + "[+] " + message + "...")
    Logger.step_depth += Logger.step_factor
    Logger.start_time.append(timer())

  def done(self, message=""):
    stop_time = timer()
    time_elapsed = stop_time - Logger.start_time.pop()
    Logger.step_depth -= Logger.step_factor
    self.print((" " * Logger.step_depth) + f"[-] DONE! (%.5fs) %s" % (time_elapsed, ""))