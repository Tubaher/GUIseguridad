import os

path_to_cache = "output/"
tmp_log_file = "output_server"
b = 5

cmd = 'vw --loss_function logistic --cache_file {} -b {} 2>&1 | tee {}'.format( 
    path_to_cache, b, tmp_log_file )
os.system( cmd )
output = open( tmp_log_file, 'r' ).read()

for line in output:
    print(line)