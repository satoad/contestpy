import asyncio

class FilterQueue(asyncio.Queue):
    def __init__(self, *args):
        super().__init__(*args)
        if len(args) != 0:
            self.window = args[0]
        else:
            self.window = None

    def __contains__(self, fltr):
        for i in self._queue:
            if fltr(i):
                return True
        return False

    def window_el(self):
        if len(self._queue) != 0:
            self.window = self._queue[0]
        else:
            self.window = None

    async def put(self, val):
        await super().put(val)
        self.window_el()

    def later(self):
        if self.window is None:
            raise asyncio.QueueEmpty
        else:
            self.put_nowait(self.get_nowait())
            self.window_el()

    async def get_ret(self):
        j = await super().get()
        self.window_el()
        return j

    async def get(self, fltr=None):
        if fltr is not None and fltr in self:
            for _ in range(len(self._queue)):
                if fltr is None:
                    break

                j = await super().get()
                if fltr(j):
                    self.window_el()
                    return j
                await super().put(j)

        j = await super().get()
        self.window_el()
        return j