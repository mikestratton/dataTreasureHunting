import java.util.*;
import java.io.*;


public class replaceCharacter
{  
    public static void main(String[] args)  
   {
   
   Scanner console = new Scanner(System.in);           
   System.out.println("File to be read: ");
   String inputFile = console.next();
   File file = new File(inputFile);
   Scanner in = new Scanner(file);

   while(in.hasNextLine()){  // while there is a next line
    String line = scanner.nextLine();  // line = that next line

    // do something with that line
    String newLine = " ";

    // replace a character
    for (int i = 0; i < line.length(); i++){
        if (line.charAt(i) != '*') {  // or anything other character you chose
            newLine += line.charAt(i);
        }
    }

    // print to another file.
    writer.println(newLine);
}

}
}