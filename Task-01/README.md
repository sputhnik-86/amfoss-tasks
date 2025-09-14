This task is for learning the basics of terminal and git commands

APPROACH:

I had learnt the linux terminal commands from the given resourse and from youtube. 

->Subtask-1:
I navigated into the earth directory by ls -a and cd commands.By using grep -r "facility" command i found Russia/Vladimir_Oblast/.facility/gravity_equation.txt.Successfully i
found my first flag by opening gravity_equation.txt file by using cat command.

->Subtask-2:
I leaved earth and navigated into the ring's of saturn by using ls -a and cd commands.I found the hidden wormhole file by using ls -a command.Made the wormhole.sh file executable by
using chmod +x command and run the file using ./ command.Successfully I found my second flag

->Subtask-3:
I used git checkout command for changing branches and git branch for viewing branches.I entered Gargantuansystem and find the habitable planet.

->Subtask-4:
I navigated into the the_core directory and opened the file message_from_Them.txt.I found the base 64 code in terms of binary.I converted the binary into ASC||.I decoded the base 64
code using echo "string" | base64 -d and got the final answer.

Commands learned:

cd <directory>:changes the current working directory to the specified directory

ls: Lists files and directories present in current directory

ls -a: Lists including hidden files and directories
   
grep:Searches for Specific text within files

grep -r "string":Search recursively within a directory

cat:Open and Outputs the contents of a file

chmod +x : Modifies the permissions and make the file executable.

./ : Runs the file

git branch : Lists all branches

git checkout <branch>:switches the branch

git clone <url>: Clones the repository from the specified url

git add : Stages the specified file for commit

echo "string" : prints the given string

nano filename : create and edit the file

mkdir : creates a new directory

    	
   
   
