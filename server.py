from gensim.models.keyedvectors import KeyedVectors

path = "/Users/pranavj/gensim-data/word2vec-google-news-300/word2vec-google-news-300.gz"
model = KeyedVectors.load_word2vec_format(path, binary=True)
print("done loading")

# print(model.similarity("cat","cinnamon"))
# print(model.similarity("cat","feline"))
# print(model.similarity("dog","water"))


import asyncio

import websockets


async def handler(websocket):
    while True:
        try:
            message = await websocket.recv()
        except websockets.ConnectionClosedOK:
            break
        print(message)
        print(model.similarity("cat", message))


async def main():
    async with websockets.serve(handler, "", 8001):
        await asyncio.Future()  # run forever


if __name__ == "__main__":
    asyncio.run(main())