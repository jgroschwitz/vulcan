import re

import penman
from vulcan.server.server import Server

if __name__ == "__main__":

    # graphs = [penman.codec.PENMANCodec().decode("(t / test)")]
    #
    # print(len(graphs))
    # print(graphs[0])
    #
    # server = Server(graphs)
    # server.start()

    print(re.compile("dog").match("dog."))
