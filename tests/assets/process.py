from barfi.st_flow import Block


def feed_func(self):
    self.set_interface(name="Output 1", value=4)


feed = Block(name="Feed")
feed.add_output()
feed.add_compute(feed_func)


def splitter_func(self):
    in_1 = self.get_interface(name="Input 1")
    value = in_1 / 2
    self.set_interface(name="Output 1", value=value)
    self.set_interface(name="Output 2", value=value)


splitter = Block(name="Splitter")
splitter.add_input()
splitter.add_output()
splitter.add_output()
splitter.add_compute(splitter_func)


def mixer_func(self):
    in_1 = self.get_interface(name="Input 1")
    in_2 = self.get_interface(name="Input 2")
    value = in_1 + in_2
    self.set_interface(name="Output 1", value=value)


mixer = Block(name="Mixer")
mixer.add_input()
mixer.add_input()
mixer.add_output()
mixer.add_compute(mixer_func)


def result_func(self):
    _ = self.get_interface(name="Input 1")


result = Block(name="Result")
result.add_input()
result.add_compute(result_func)

process_blocks = [feed, result, mixer, splitter]
