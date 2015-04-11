import java.util.*;
import java.io.*;

public class wordCountNLP2
{  
    public static void main(String[] args) throws FileNotFoundException 
   {
      HashMap map = new HashMap();  
      Scanner console = new Scanner(System.in);           
      System.out.println("File to be read: ");
      String inputFile = console.next();
      File file = new File(inputFile);
      Scanner in = new Scanner(file);
      
      while(console.hasNextLine()){  // while there is a next line
    String line = in.nextLine();  // line = that next line

    // do something with that line
    //String newLine;
    String newLine = "c";
    
          // replace a character
    for (int i = 0; i < line.length(); i++){
        if (line.charAt(i) != 'a') {  // or anything other character you chose
            newLine += line.charAt(i);
        }
    }

       
      Scanner output = new Scanner(System.in);           
      System.out.println("Please select output file name: ");
      String outputFile = output.next();
      

         ArrayList arraylist = new ArrayList(map.keySet());
         Collections.sort(arraylist);     

            String fileName = outputFile;
            
            try {
               PrintWriter outputStream = new PrintWriter(fileName);
               for (int i = 0; i < arraylist.size(); i++) 
               {
                  String key = (String)arraylist.get(i);
                  Integer count = (Integer)map.get(key);
               
               outputStream.println(key + ";" + count);
               }   
               outputStream.close();
               System.out.println("Execution complete");
            } 
               catch (FileNotFoundException e){
                  e.printStackTrace(); 
               }              
    }  


}
}