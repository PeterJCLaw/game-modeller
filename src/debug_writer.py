
import json

class DebugWriter(object):
    def __init__(self, wrap):
        self.wrap = wrap
        self._buffer = ''

    def write(self, s):
        self._buffer += s
        if '\n' in self._buffer:
            self.flush()

    def flush(self):
        for line in self._buffer.split('\n'):
            # ignore empty lines
            if len(line.strip()) == 0:
                continue
            msg = dict(type = 'debug', message = line)
            json_msg = json.dumps(msg)
            self.wrap.write(json_msg + '\n')

        self._buffer = ''
        self.wrap.flush()
