import os,subprocess,tempfile,unittest
from pathlib import Path
class Install(unittest.TestCase):
 def test_first_install_game_path_appears_after_apt(self):
  with tempfile.TemporaryDirectory() as d:
   root=Path(d);bin=root/'bin';bin.mkdir();game=root/'games'/'moon-buggy';game.parent.mkdir();flag=root/'installed'
   # Isolated fixture substitutes /usr/games only in this test copy.
   script=root/'app-store.sh';script.write_text((Path(__file__).parent/'app-store.sh').read_text().replace('/usr/games/moon-buggy',str(game)))
   commands={'id':'echo 0','dpkg-query':'[ -f "$FLAG" ] && echo "install ok installed" || exit 1','apt-cache':'echo "Candidate: 1.0.51"','apt-get':'if [ "$1" = install ]; then touch "$FLAG"; printf "#!/bin/bash\\nexit 0\\n" > "$GAME"; chmod +x "$GAME"; fi'}
   for name,body in commands.items():
    path=bin/name;path.write_text('#!/bin/bash\n'+body+'\n');path.chmod(0o755)
   env=dict(os.environ,PATH=str(bin)+':/usr/bin:/bin',FLAG=str(flag),GAME=str(game))
   r=subprocess.run(['bash',str(script),'install'],env=env,capture_output=True,text=True)
   self.assertEqual(r.returncode,0,r.stdout+r.stderr);self.assertTrue(game.exists())
   r=subprocess.run(['bash',str(script),'status'],env=env,capture_output=True,text=True);self.assertEqual(r.returncode,0)
if __name__=='__main__':unittest.main()
