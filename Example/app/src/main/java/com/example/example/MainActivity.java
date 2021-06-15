package com.example.example;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Context;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

import org.w3c.dom.Text;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class MainActivity extends AppCompatActivity {
    private Button btnTest;
    private TextView textView1;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        btnTest = (Button) findViewById(R.id.btnTest);
        textView1 = (TextView) findViewById(R.id.textView1);

        btnTest.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                try{
                    writeFile("testFile.txt", "testtttttt");
                    String rFile = readFile("testFile.txt");
                    textView1.setText(rFile);
                }catch(IOException e){
                    e.printStackTrace();
                }
            }
        });
    }

    private void writeFile(String fileName, String msg){
        try{
            OutputStreamWriter oStreamWriter = new OutputStreamWriter(openFileOutput(fileName,
                    Context.MODE_PRIVATE));
            oStreamWriter.write(msg);
            oStreamWriter.close();
        } catch(FileNotFoundException e){
            e.printStackTrace();
        } catch(IOException e){
            e.printStackTrace();
        }
    }

    private String readFile(String fileName) throws IOException{
        String fileContents = "";
        try{
            InputStream iStream = openFileInput(fileName);
            if(iStream != null) {
                InputStreamReader iStreamReader = new InputStreamReader(iStream);
                BufferedReader bufferedReader = new BufferedReader(iStreamReader);
                String temp = "";
                StringBuffer sBuffer = new StringBuffer();
                while ((temp = bufferedReader.readLine()) != null) {
                    sBuffer.append(temp);
                }
                iStream.close();
                fileContents = sBuffer.toString();
            }
        } catch(FileNotFoundException e){
            e.printStackTrace();
        }
        return fileContents;
    }
}