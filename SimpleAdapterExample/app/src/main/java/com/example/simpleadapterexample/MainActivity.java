package com.example.simpleadapterexample;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.ListView;
import android.widget.SimpleAdapter;
import android.widget.Toast;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

public class MainActivity extends AppCompatActivity {
    private ListView listView;

    ArrayList<HashMap<String, String>> data;
    HashMap<String, String> numberList;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        listView = (ListView) findViewById(R.id.listView);
        data = new ArrayList<HashMap<String, String>>();

        numberList = new HashMap<String, String>();
        numberList.put("Name", "Zero");
        numberList.put("Number", "0");
        data.add(numberList);

        numberList = new HashMap<String, String>();
        numberList.put("Name", "One");
        numberList.put("Number", "1");
        data.add(numberList);

        numberList = new HashMap<String, String>();
        numberList.put("Name", "Two");
        numberList.put("Number", "2");
        data.add(numberList);

        numberList = new HashMap<String, String>();
        numberList.put("Name", "Three");
        numberList.put("Number", "3");
        data.add(numberList);

        numberList = new HashMap<String, String>();
        numberList.put("Name", "Four");
        numberList.put("Number", "4");
        data.add(numberList);

        numberList = new HashMap<String, String>();
        numberList.put("Name", "Five");
        numberList.put("Number", "5");
        data.add(numberList);

        numberList = new HashMap<String, String>();
        numberList.put("Name", "Six");
        numberList.put("Number", "6");
        data.add(numberList);

        numberList = new HashMap<String, String>();
        numberList.put("Name", "seven");
        numberList.put("Number", "7");
        data.add(numberList);

        numberList = new HashMap<String, String>();
        numberList.put("Name", "Eight");
        numberList.put("Number", "8");
        data.add(numberList);

        numberList = new HashMap<String, String>();
        numberList.put("Name", "Nine");
        numberList.put("Number", "9");
        data.add(numberList);

        SimpleAdapter adapter = new SimpleAdapter(
                getApplicationContext(),
                data,
                android.R.layout.simple_list_item_2,
                new String[]{"Name", "Number"},
                new int[]{android.R.id.text1, android.R.id.text2}
        );

        listView.setAdapter(adapter);
    }
}