from apps import app,db
from flask_script import Manager,Shell
from flask_migrate import Migrate,MigrateCommand


manager = Manager(app)
migrate = Migrate(app,db)

def make_shell_context():

    manager.add_command("shell", Shell(make_context=make_shell_context))
    manager.add_command('db', MigrateCommand)
    return dict(app=app, db=db)



if __name__ == "__main__":
    #添加python manage.py 的命令参数 默认只有shell runserver
    make_shell_context()
    manager.run()