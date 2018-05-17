import os

cmd1 = 'bundle install'
cmd2 = 'bundle exec jekyll serve --config _config.yml'

os.system(cmd1)
os.system(cmd2)
