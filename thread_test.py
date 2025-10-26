import threading, zipfile

class AsyncZip(threading.Thread):
    def __init__(self, infile, outfile):
        threading.Thread.__init__(self)
        self.infile = infile
        self.outfile = outfile

    def run(self):
        f = zipfile.ZipFile(self.outfile, 'w', zipfile.ZIP_DEFLATED)
        f.write(self.infile)
        f.close()
        print(f"Zipped {self.infile} to {self.outfile}")

async_zip = AsyncZip('mydata.txt', 'myarchive.zip')
async_zip.start()
print('Waiting for async_zip to complete...')
async_zip.join()
print('Main program continues to run in foreground.')
