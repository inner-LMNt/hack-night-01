from gensim.models.keyedvectors import KeyedVectors

path = "/Users/pranavj/gensim-data/word2vec-google-news-300/word2vec-google-news-300.gz"

# To download the model, uncomment the following lines:
# DO NOT COMMIT THESE LINES UNCOMMENTED
# import gensim.downloader as api
# path = api.load("word2vec-google-news-300", return_path=True)
# print(path)

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
        try:
            score = model.similarity("cat", message)
            print(score)
            
        except:
            print('invalid input')
            score = -1
        await websocket.send(str(score))

async def main():
    async with websockets.serve(handler, "", 8001):
        await asyncio.Future()  # run forever


if __name__ == "__main__":
    asyncio.run(main())