package Triangle.ProgramWriter;

import java.io.File;
import java.io.FileWriter;
import java.io.IOException;

public class HTMLWriter {

    private FileWriter fileWriter;

    public HTMLWriter(String sourcename){
        File dir = new File("output" + File.separator);
        dir.mkdirs();

        File htmlFile = new File(dir, sourcename.concat(".html");

        try{
            fileWriter = new FileWriter(htmlFile);

            writeToHTMLFile("<!DOCTYPE html>");
            writeToHTMLFile("\n");
            writeToHTMLFile("<html>");
            writeToHTMLFile("\n");
            writeToHTMLFile("< style=\"font-family: monospace; font-size:160%;\">");
        }
        catch (IOException e){
            e.printStackTrace();
        }
    }

    public void WriteKeyWord(String keyword){writeToHTMLFile("<b>"+keyword+"</b>");

}
