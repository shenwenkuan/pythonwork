import fire

class Example(object):
    def Hello(self, name='world'):
        return 'hello {world}!'.format(name=name)

def main():
    fire.Fire(Example)

if __name__ == '__main__':
    main()