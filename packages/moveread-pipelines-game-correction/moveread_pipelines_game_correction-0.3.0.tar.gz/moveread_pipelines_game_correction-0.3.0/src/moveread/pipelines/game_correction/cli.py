from argparse import ArgumentParser

def main():
  parser = ArgumentParser()
  parser.add_argument('-i', '--images', required=True, type=str)
  parser.add_argument('-d', '--db', required=True, type=str)

  parser.add_argument('-p', '--port', default=8000, type=int)
  parser.add_argument('--host', default='0.0.0.0', type=str)
  parser.add_argument('--url', default=None, help='Base URL for the API')

  args = parser.parse_args()

  import os
  from dslog import Logger

  db_path = os.path.join(os.getcwd(), args.db)

  logger = Logger.click().prefix('[GAME CORRECTION]')
  logger(f'Running API...')
  logger(f'- DB path: "{db_path}"')
  logger(f'- Images connection string: "{args.images}"')

  from fastapi.middleware.cors import CORSMiddleware
  import uvicorn
  from kv import KV, LocatableKV, ServerKV, SQLiteKV
  from pipeteer import QueueKV
  from moveread.pipelines.game_correction import GameCorrection, Output, Annotations

  def get_queue(path, type):
    return QueueKV.sqlite(type, db_path, '-'.join(['queue', *path]))
  
  images = KV[bytes].of(args.images)
  if not isinstance(images, LocatableKV):
    if not args.url:
      raise ValueError('Provide a LocatableKV (--images) or a base URL (--url)')
    images = images.served(args.url.rstrip('/') + '/images')

  Qout = get_queue(('output',), Output)
  pipe = GameCorrection()
  cache = SQLiteKV.at(db_path, Annotations, table='cache')
  params = GameCorrection.Params(images=images, logger=logger, cache=cache)
  Qs = pipe.connect(Qout, get_queue, params)
  api = pipe.run(Qs, params)
  api.mount('/images', ServerKV(images))
  api.add_middleware(CORSMiddleware, allow_origins=['*'], allow_methods=['*'], allow_headers=['*'])
  
  uvicorn.run(api, port=args.port, host=args.host)
  
if __name__ == '__main__':
  import sys
  sys.argv.extend('-p 8001 -i demo/images -q demo/queues.sqlite'.split(' '))
  main()