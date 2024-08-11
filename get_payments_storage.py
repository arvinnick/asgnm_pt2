############
#
# Streaming Payments Processor
#
# The function `process_payments()` is processing a large, but finite amount of payments in a streaming fashion.
#
# It relies on two library functions to do its job. The first function `stream_payments_to_storage(storage)` reads the
# payments from a payment processor and writes them to storage by calling `storage.write(buffer)` on it's `storage`
# argument. The `storage` argument is supplied by calling `get_payments_storage()` function. The API is defined below.
#
#
# The checksum is implemented as a simple arithmetic sum of bytes.
#
# For example, if bytes([1, 2, 3]) were written, you should print 6.
#
#
# NOTE: you need to take into account the following restrictions:
# - You are allowed only one call each to `get_payments_storage()` and
# to `stream_payments_to_storage()`
# - You can not read from the storage.
# - You can not use disk as temporary storage.
# - Your system has limited memory that can not hold all payments.
#
############

from io import BufferedWriter


# This is a library function, you can't modify it.
def get_payments_storage():
    """
    @returns an instance of
    https://docs.python.org/3/library/io.html#io.BufferedWriter
    """
    # Sample implementation to make the code run in coderpad.
    # Do not rely on this exact implementation.
    return open('./null', 'wb')


# This is a library function, you can't modify it.
def stream_payments_to_storage(storage):
    """
    Loads payments and writes them to the `storage`.
    Returns when all payments have been written.
    @parameter `storage`: is an instance of
    https://docs.python.org/3/library/io.html#io.BufferedWriter
    """
    # Sample implementation to make the code run in coderpad.
    # Do not rely on this exact implementation.
    for i in range(10):
        storage.write(bytes([1, 2, 3, 4, 5]))


class StoredStream(BufferedWriter):
    def __init__(self, raw):
        super().__init__(raw)
        self.checksum = 0

    def write(self, data):
        self.checksum += sum(data)
        return super().write(data)


def process_payments():
    """
    """

    buffer = StoredStream(get_payments_storage())
    stream_payments_to_storage(buffer)
    # Here print the check sum of all the bytes written by `stream_payments_to_storage()`
    print(buffer.checksum)


process_payments()
