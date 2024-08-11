############
# Streaming Payments Processor, two vendors edition.
#
# We decided to improve the payment processor from the previous exercise and hired two vendors. One was to implement
# `stream_payments()` function, and another `store_payments()` function.
#
# The function `process_payments_2()` is processing a large, but finite amount of payments in a streaming fashion.
#
# Unfortunately the vendors did not coordinate their efforts, and delivered their functions with incompatible APIs.
#
# TODO: Your task is to analyse the APIs of `stream_payments()` and `store_payments()` and to write glue code in
#  `process_payments_2()` that allows us to store the payments using these vendor functions.
#
# NOTE: you need to take into account the following restrictions:
# - You are allowed only one call each to `stream_payments()` and to `store_payments()`
# - You can not read from the storage.
# - You can not use disk as temporary storage.
# - Your system has limited memory that can not hold all payments.
#
############

# This is a library function, you can't modify it.
def stream_payments(callback_fn):
    """
    Reads payments from a payment processor and calls `callback_fn(amount)`
    for each payment.
    Returns when there is no more payments.
    """
    # Sample implementation to make the code run in coderpad.
    # Do not rely on this exact implementation.
    for i in range(10):
        callback_fn(i)
    # This is a library function, you can't modify it.


def store_payments(amount_iterator):
    """
    Iterates over the payment amounts from amount_iterator
    and stores them to a remote system.
    """
    # Sample implementation to make the code run in coderpad.
    # Do not rely on this exact implementation.
    for i in amount_iterator:
        print(i)


# def callback_example(amount):
#     print(amount)
#     return True




def process_payments_2():
    """
    TODO: Modify `process_payments_2()`, write glue code that enables `store_payments()` to consume payments produced
       by `stream_payments()`
    """

    def callback_fn(obj):
        """
        stores the obj in a global variable
        """
        store_payments([obj])
    stream_payments(callback_fn)


process_payments_2()
