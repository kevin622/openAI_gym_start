# Tutorial for Open AI Gym

This repository is results of following tutorials of [documents of open AI gym](https://gym.openai.com/docs/).

## Setting up virtual environment

```bash
$ python -m venv venv
$ source venv/bin/activate
(venv) $ pip list
Package    Version
---------- -------
pip        20.2.3
setuptools 49.2.1
```

With the codes above, I've made a `venv` file. All libraries or packages will be placed here.

I installed the `gym` package here.

```bash
(venv) $ pip install gym
```

## CartPole-v0

Made a file named `cart_pole.py` and wrote as the tutorial.

```python
import gym
env = gym.make('CartPole-v0')
env.reset()
for _ in range(100):
    env.render()
    env.step(env.action_space.sample())
env.close()
```

However, I recieved an ImportError trying to run this, saying `Cannot import pyglet.` 
So I installed `pyglet` and ran successfully.

```bash
(venv) $ pip install pyglet
(venv) $ python cart_pole.py
```

By making files whose input for `gym.make` function is different, I've tried other environments as well.

## MountainCar-v0

Made another file named `mountain_car.py` and wrote as such.

```python
import gym
env = gym.make('MountainCar-v0')
env.reset()
for _ in range(100):
    env.render()
    env.step(env.action_space.sample())
env.close()
```

## MsPacman-v0

Made another file named `ms_pacman.py` and wrote as such.

```python
import gym
env = gym.make('MsPacman-v0')
env.reset()
for _ in range(100):
    env.render()
    env.step(env.action_space.sample())
env.close()
```

However, I've faced error saying `gym.error.UnregisteredEnv: No registered env with id: MsPacman-v0`.

## Mujoco(error)

The official document said running `pip install gym[all]` would install all dependencies needed, but after some trials and errors, I found that the right command is `pip install gym\[all\]`.
But after this command, I faced another error saying

```bash
Please follow the instructions on the README to install MuJoCo
    
https://github.com/openai/mujoco-py#install-mujoco
```

So I went to the [link](https://github.com/openai/mujoco-py#install-mujoco) and followed as such;

1. Downloaded the bin file for Mujoco and placed it in `~/.mujoco/mujoco210` 
2. Ran the command `pip install -U 'mujoco-py<2.2,>=2.1`.

But even after that, I still get a long error message which is hard to interpret.

```bash
running build_ext
building 'mujoco_py.cymj' extension
/usr/local/bin/gcc-9 -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -I/Library/Developer/CommandLineTools/SDKs/MacOSX10.15.sdk/usr/include -I/Library/Developer/CommandLineTools/SDKs/MacOSX10.15.sdk/usr/include -DONMAC -Ivenv/lib/python3.8/site-packages/mujoco_py -I/Users/duru/openAI_gym_start/venv/lib/python3.8/site-packages/mujoco_py -I/Users/duru/.mujoco/mujoco210/include -I/Users/duru/openAI_gym_start/venv/lib/python3.8/site-packages/numpy/core/include -I/Users/duru/openAI_gym_start/venv/include -I/Users/duru/.pyenv/versions/3.8.7/include/python3.8 -c /Users/duru/openAI_gym_start/venv/lib/python3.8/site-packages/mujoco_py/cymj.c -o /Users/duru/openAI_gym_start/venv/lib/python3.8/site-packages/mujoco_py/generated/_pyxbld_2.1.2.14_38_macextensionbuilder/temp.macosx-10.15-x86_64-3.8/Users/duru/openAI_gym_start/venv/lib/python3.8/site-packages/mujoco_py/cymj.o -fopenmp -w
In file included from /usr/local/Cellar/gcc/9.3.0_1/lib/gcc/9/gcc/x86_64-apple-darwin18/9.3.0/include-fixed/syslimits.h:7,
                 from /usr/local/Cellar/gcc/9.3.0_1/lib/gcc/9/gcc/x86_64-apple-darwin18/9.3.0/include-fixed/limits.h:34,
                 from /Users/duru/.pyenv/versions/3.8.7/include/python3.8/Python.h:11,
                 from /Users/duru/openAI_gym_start/venv/lib/python3.8/site-packages/mujoco_py/cymj.c:63:
/usr/local/Cellar/gcc/9.3.0_1/lib/gcc/9/gcc/x86_64-apple-darwin18/9.3.0/include-fixed/limits.h:194:61: error: no include path in which to search for limits.h
  194 | #include_next <limits.h>  /* recurse down to the real one */
      |                                                             ^
In file included from /Users/duru/.pyenv/versions/3.8.7/include/python3.8/Python.h:25,
                 from /Users/duru/openAI_gym_start/venv/lib/python3.8/site-packages/mujoco_py/cymj.c:63:
/usr/local/Cellar/gcc/9.3.0_1/lib/gcc/9/gcc/x86_64-apple-darwin18/9.3.0/include-fixed/stdio.h:78:10: fatal error: _stdio.h: No such file or directory
   78 | #include <_stdio.h>
      |          ^~~~~~~~~~
compilation terminated.
Traceback (most recent call last):
  File "/Users/duru/.pyenv/versions/3.8.7/lib/python3.8/distutils/unixccompiler.py", line 117, in _compile
    self.spawn(compiler_so + cc_args + [src, '-o', obj] +
  File "/Users/duru/.pyenv/versions/3.8.7/lib/python3.8/distutils/ccompiler.py", line 910, in spawn
    spawn(cmd, dry_run=self.dry_run)
  File "/Users/duru/.pyenv/versions/3.8.7/lib/python3.8/distutils/spawn.py", line 36, in spawn
    _spawn_posix(cmd, search_path, dry_run=dry_run)
  File "/Users/duru/.pyenv/versions/3.8.7/lib/python3.8/distutils/spawn.py", line 157, in _spawn_posix
    raise DistutilsExecError(
distutils.errors.DistutilsExecError: command '/usr/local/bin/gcc-9' failed with exit status 1

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "hopper.py", line 2, in <module>
    env = gym.make('Hopper-v2')
  File "/Users/duru/openAI_gym_start/venv/lib/python3.8/site-packages/gym/envs/registration.py", line 235, in make
    return registry.make(id, **kwargs)
  File "/Users/duru/openAI_gym_start/venv/lib/python3.8/site-packages/gym/envs/registration.py", line 129, in make
    env = spec.make(**kwargs)
  File "/Users/duru/openAI_gym_start/venv/lib/python3.8/site-packages/gym/envs/registration.py", line 89, in make
    cls = load(self.entry_point)
  File "/Users/duru/openAI_gym_start/venv/lib/python3.8/site-packages/gym/envs/registration.py", line 27, in load
    mod = importlib.import_module(mod_name)
  File "/Users/duru/.pyenv/versions/3.8.7/lib/python3.8/importlib/__init__.py", line 127, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1014, in _gcd_import
  File "<frozen importlib._bootstrap>", line 991, in _find_and_load
  File "<frozen importlib._bootstrap>", line 975, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 671, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 783, in exec_module
  File "<frozen importlib._bootstrap>", line 219, in _call_with_frames_removed
  File "/Users/duru/openAI_gym_start/venv/lib/python3.8/site-packages/gym/envs/mujoco/__init__.py", line 1, in <module>
    from gym.envs.mujoco.mujoco_env import MujocoEnv
  File "/Users/duru/openAI_gym_start/venv/lib/python3.8/site-packages/gym/envs/mujoco/mujoco_env.py", line 12, in <module>
    import mujoco_py
  File "/Users/duru/openAI_gym_start/venv/lib/python3.8/site-packages/mujoco_py/__init__.py", line 2, in <module>
    from mujoco_py.builder import cymj, ignore_mujoco_warnings, functions, MujocoException
  File "/Users/duru/openAI_gym_start/venv/lib/python3.8/site-packages/mujoco_py/builder.py", line 504, in <module>
    cymj = load_cython_ext(mujoco_path)
  File "/Users/duru/openAI_gym_start/venv/lib/python3.8/site-packages/mujoco_py/builder.py", line 110, in load_cython_ext
    cext_so_path = builder.build()
  File "/Users/duru/openAI_gym_start/venv/lib/python3.8/site-packages/mujoco_py/builder.py", line 226, in build
    built_so_file_path = self._build_impl()
  File "/Users/duru/openAI_gym_start/venv/lib/python3.8/site-packages/mujoco_py/builder.py", line 340, in _build_impl
    so_file_path = super()._build_impl()
  File "/Users/duru/openAI_gym_start/venv/lib/python3.8/site-packages/mujoco_py/builder.py", line 249, in _build_impl
    dist.run_commands()
  File "/Users/duru/.pyenv/versions/3.8.7/lib/python3.8/distutils/dist.py", line 966, in run_commands
    self.run_command(cmd)
  File "/Users/duru/.pyenv/versions/3.8.7/lib/python3.8/distutils/dist.py", line 985, in run_command
    cmd_obj.run()
  File "/Users/duru/openAI_gym_start/venv/lib/python3.8/site-packages/Cython/Distutils/old_build_ext.py", line 186, in run
    _build_ext.build_ext.run(self)
  File "/Users/duru/.pyenv/versions/3.8.7/lib/python3.8/distutils/command/build_ext.py", line 340, in run
    self.build_extensions()
  File "/Users/duru/openAI_gym_start/venv/lib/python3.8/site-packages/mujoco_py/builder.py", line 149, in build_extensions
    build_ext.build_extensions(self)
  File "/Users/duru/openAI_gym_start/venv/lib/python3.8/site-packages/Cython/Distutils/old_build_ext.py", line 195, in build_extensions
    _build_ext.build_ext.build_extensions(self)
  File "/Users/duru/.pyenv/versions/3.8.7/lib/python3.8/distutils/command/build_ext.py", line 449, in build_extensions
    self._build_extensions_serial()
  File "/Users/duru/.pyenv/versions/3.8.7/lib/python3.8/distutils/command/build_ext.py", line 474, in _build_extensions_serial
    self.build_extension(ext)
  File "/Users/duru/.pyenv/versions/3.8.7/lib/python3.8/distutils/command/build_ext.py", line 528, in build_extension
    objects = self.compiler.compile(sources,
  File "/Users/duru/.pyenv/versions/3.8.7/lib/python3.8/distutils/ccompiler.py", line 574, in compile
    self._compile(obj, src, ext, cc_args, extra_postargs, pp_opts)
  File "/Users/duru/.pyenv/versions/3.8.7/lib/python3.8/distutils/unixccompiler.py", line 120, in _compile
    raise CompileError(msg)
distutils.errors.CompileError: command '/usr/local/bin/gcc-9' failed with exit status 1
```



Still working on finding the problem...

This maybe due to not having Xcode installed referring to [this](https://nkaushik.com/mac/mac-c-compilation-error/) according to the line which says

```bash
/usr/local/Cellar/gcc/9.3.0_1/lib/gcc/9/gcc/x86_64-apple-darwin18/9.3.0/include-fixed/stdio.h:78:10: fatal error: _stdio.h: No such file or directory
   78 | #include <_stdio.h>
      |          ^~~~~~~~~~
compilation terminated.
```

So I'm trying installing it via

```bash
xcode-select --install
```

Installation took about 20 minutes, but still errors is causing when trying to run `hopper.py`

```bash
running build_ext
building 'mujoco_py.cymj' extension
/usr/local/bin/gcc-9 -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -I/Library/Developer/CommandLineTools/SDKs/MacOSX10.15.sdk/usr/include -I/Library/Developer/CommandLineTools/SDKs/MacOSX10.15.sdk/usr/include -DONMAC -Ivenv/lib/python3.8/site-packages/mujoco_py -I/Users/duru/openAI_gym_start/venv/lib/python3.8/site-packages/mujoco_py -I/Users/duru/.mujoco/mujoco210/include -I/Users/duru/openAI_gym_start/venv/lib/python3.8/site-packages/numpy/core/include -I/Users/duru/openAI_gym_start/venv/include -I/Users/duru/.pyenv/versions/3.8.7/include/python3.8 -c /Users/duru/openAI_gym_start/venv/lib/python3.8/site-packages/mujoco_py/cymj.c -o /Users/duru/openAI_gym_start/venv/lib/python3.8/site-packages/mujoco_py/generated/_pyxbld_2.1.2.14_38_macextensionbuilder/temp.macosx-10.15-x86_64-3.8/Users/duru/openAI_gym_start/venv/lib/python3.8/site-packages/mujoco_py/cymj.o -fopenmp -w
/usr/local/bin/gcc-9 -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -I/Library/Developer/CommandLineTools/SDKs/MacOSX10.15.sdk/usr/include -I/Library/Developer/CommandLineTools/SDKs/MacOSX10.15.sdk/usr/include -DONMAC -Ivenv/lib/python3.8/site-packages/mujoco_py -I/Users/duru/openAI_gym_start/venv/lib/python3.8/site-packages/mujoco_py -I/Users/duru/.mujoco/mujoco210/include -I/Users/duru/openAI_gym_start/venv/lib/python3.8/site-packages/numpy/core/include -I/Users/duru/openAI_gym_start/venv/include -I/Users/duru/.pyenv/versions/3.8.7/include/python3.8 -c /Users/duru/openAI_gym_start/venv/lib/python3.8/site-packages/mujoco_py/gl/dummyshim.c -o /Users/duru/openAI_gym_start/venv/lib/python3.8/site-packages/mujoco_py/generated/_pyxbld_2.1.2.14_38_macextensionbuilder/temp.macosx-10.15-x86_64-3.8/Users/duru/openAI_gym_start/venv/lib/python3.8/site-packages/mujoco_py/gl/dummyshim.o -fopenmp -w
creating /Users/duru/openAI_gym_start/venv/lib/python3.8/site-packages/mujoco_py/generated/_pyxbld_2.1.2.14_38_macextensionbuilder/lib.macosx-10.15-x86_64-3.8
creating /Users/duru/openAI_gym_start/venv/lib/python3.8/site-packages/mujoco_py/generated/_pyxbld_2.1.2.14_38_macextensionbuilder/lib.macosx-10.15-x86_64-3.8/mujoco_py
/usr/local/bin/gcc-9 -bundle -undefined dynamic_lookup -L/usr/local/opt/readline/lib -L/usr/local/opt/readline/lib -L/Users/duru/.pyenv/versions/3.8.7/lib -L/usr/local/opt/readline/lib -L/usr/local/opt/readline/lib -L/Users/duru/.pyenv/versions/3.8.7/lib /Users/duru/openAI_gym_start/venv/lib/python3.8/site-packages/mujoco_py/generated/_pyxbld_2.1.2.14_38_macextensionbuilder/temp.macosx-10.15-x86_64-3.8/Users/duru/openAI_gym_start/venv/lib/python3.8/site-packages/mujoco_py/cymj.o /Users/duru/openAI_gym_start/venv/lib/python3.8/site-packages/mujoco_py/generated/_pyxbld_2.1.2.14_38_macextensionbuilder/temp.macosx-10.15-x86_64-3.8/Users/duru/openAI_gym_start/venv/lib/python3.8/site-packages/mujoco_py/gl/dummyshim.o -L/Users/duru/.mujoco/mujoco210/bin -L/Users/duru/.mujoco/mujoco210/bin -lmujoco210 -lglfw.3 -o /Users/duru/openAI_gym_start/venv/lib/python3.8/site-packages/mujoco_py/generated/_pyxbld_2.1.2.14_38_macextensionbuilder/lib.macosx-10.15-x86_64-3.8/mujoco_py/cymj.cpython-38-darwin.so -fopenmp
ld: library not found for -lSystem
collect2: error: ld returned 1 exit status
Traceback (most recent call last):
  File "/Users/duru/.pyenv/versions/3.8.7/lib/python3.8/distutils/unixccompiler.py", line 204, in link
    self.spawn(linker + ld_args)
  File "/Users/duru/.pyenv/versions/3.8.7/lib/python3.8/distutils/ccompiler.py", line 910, in spawn
    spawn(cmd, dry_run=self.dry_run)
  File "/Users/duru/.pyenv/versions/3.8.7/lib/python3.8/distutils/spawn.py", line 36, in spawn
    _spawn_posix(cmd, search_path, dry_run=dry_run)
  File "/Users/duru/.pyenv/versions/3.8.7/lib/python3.8/distutils/spawn.py", line 157, in _spawn_posix
    raise DistutilsExecError(
distutils.errors.DistutilsExecError: command '/usr/local/bin/gcc-9' failed with exit status 1

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "hopper.py", line 2, in <module>
    env = gym.make('Hopper-v2')
  File "/Users/duru/openAI_gym_start/venv/lib/python3.8/site-packages/gym/envs/registration.py", line 235, in make
    return registry.make(id, **kwargs)
  File "/Users/duru/openAI_gym_start/venv/lib/python3.8/site-packages/gym/envs/registration.py", line 129, in make
    env = spec.make(**kwargs)
  File "/Users/duru/openAI_gym_start/venv/lib/python3.8/site-packages/gym/envs/registration.py", line 89, in make
    cls = load(self.entry_point)
  File "/Users/duru/openAI_gym_start/venv/lib/python3.8/site-packages/gym/envs/registration.py", line 27, in load
    mod = importlib.import_module(mod_name)
  File "/Users/duru/.pyenv/versions/3.8.7/lib/python3.8/importlib/__init__.py", line 127, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1014, in _gcd_import
  File "<frozen importlib._bootstrap>", line 991, in _find_and_load
  File "<frozen importlib._bootstrap>", line 975, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 671, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 783, in exec_module
  File "<frozen importlib._bootstrap>", line 219, in _call_with_frames_removed
  File "/Users/duru/openAI_gym_start/venv/lib/python3.8/site-packages/gym/envs/mujoco/__init__.py", line 1, in <module>
    from gym.envs.mujoco.mujoco_env import MujocoEnv
  File "/Users/duru/openAI_gym_start/venv/lib/python3.8/site-packages/gym/envs/mujoco/mujoco_env.py", line 12, in <module>
    import mujoco_py
  File "/Users/duru/openAI_gym_start/venv/lib/python3.8/site-packages/mujoco_py/__init__.py", line 2, in <module>
    from mujoco_py.builder import cymj, ignore_mujoco_warnings, functions, MujocoException
  File "/Users/duru/openAI_gym_start/venv/lib/python3.8/site-packages/mujoco_py/builder.py", line 504, in <module>
    cymj = load_cython_ext(mujoco_path)
  File "/Users/duru/openAI_gym_start/venv/lib/python3.8/site-packages/mujoco_py/builder.py", line 110, in load_cython_ext
    cext_so_path = builder.build()
  File "/Users/duru/openAI_gym_start/venv/lib/python3.8/site-packages/mujoco_py/builder.py", line 226, in build
    built_so_file_path = self._build_impl()
  File "/Users/duru/openAI_gym_start/venv/lib/python3.8/site-packages/mujoco_py/builder.py", line 340, in _build_impl
    so_file_path = super()._build_impl()
  File "/Users/duru/openAI_gym_start/venv/lib/python3.8/site-packages/mujoco_py/builder.py", line 249, in _build_impl
    dist.run_commands()
  File "/Users/duru/.pyenv/versions/3.8.7/lib/python3.8/distutils/dist.py", line 966, in run_commands
    self.run_command(cmd)
  File "/Users/duru/.pyenv/versions/3.8.7/lib/python3.8/distutils/dist.py", line 985, in run_command
    cmd_obj.run()
  File "/Users/duru/openAI_gym_start/venv/lib/python3.8/site-packages/Cython/Distutils/old_build_ext.py", line 186, in run
    _build_ext.build_ext.run(self)
  File "/Users/duru/.pyenv/versions/3.8.7/lib/python3.8/distutils/command/build_ext.py", line 340, in run
    self.build_extensions()
  File "/Users/duru/openAI_gym_start/venv/lib/python3.8/site-packages/mujoco_py/builder.py", line 149, in build_extensions
    build_ext.build_extensions(self)
  File "/Users/duru/openAI_gym_start/venv/lib/python3.8/site-packages/Cython/Distutils/old_build_ext.py", line 195, in build_extensions
    _build_ext.build_ext.build_extensions(self)
  File "/Users/duru/.pyenv/versions/3.8.7/lib/python3.8/distutils/command/build_ext.py", line 449, in build_extensions
    self._build_extensions_serial()
  File "/Users/duru/.pyenv/versions/3.8.7/lib/python3.8/distutils/command/build_ext.py", line 474, in _build_extensions_serial
    self.build_extension(ext)
  File "/Users/duru/.pyenv/versions/3.8.7/lib/python3.8/distutils/command/build_ext.py", line 550, in build_extension
    self.compiler.link_shared_object(
  File "/Users/duru/.pyenv/versions/3.8.7/lib/python3.8/distutils/ccompiler.py", line 713, in link_shared_object
    self.link(CCompiler.SHARED_OBJECT, objects,
  File "/Users/duru/.pyenv/versions/3.8.7/lib/python3.8/distutils/unixccompiler.py", line 206, in link
    raise LinkError(msg)
distutils.errors.LinkError: command '/usr/local/bin/gcc-9' failed with exit status 1
```

So I'm postponing solving this problem to later...