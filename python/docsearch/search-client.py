#!/usr/bin/env python3
# coding: utf-8
if __name__ == '__main__':
    import zmq
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect('tcp://localhost:9000')

    query = ''
    while query != 'exit':
        query = input('q: ')
        socket.send_string(query)
        results = socket.recv()
        print(results)
