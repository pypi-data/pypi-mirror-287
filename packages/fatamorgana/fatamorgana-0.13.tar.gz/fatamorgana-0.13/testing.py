from io import BytesIO
import fatamorgana
failed = []
for ii in range(1, 16):
    for jj in range(1, 20):
        print(ii, jj)
        try:
            with open(f'/home/jan/software/layout/klayout-source/testdata/oasis/t{ii}.{jj}.oas', 'rb') as ff:
                aa = ff.read()
                bb = fatamorgana.OasisLayout.read(BytesIO(aa[:-253]))
        except FileNotFoundError:
            print('failed to open', ii, '.', jj)
            break
        except Exception as err:
            failed.append((ii, jj, err))

        if (ii, jj) == (9, 2):
            continue

        with open(f'/tmp/t{ii}.{jj}.oas', 'wb') as ff:
            bb.write(ff)
[print(ff) for ff in failed]
