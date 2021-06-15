package com.example.componenttest;

import android.app.Activity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

public class SecondActivity extends Activity {
    private Button btnBack;
    private TextView textViewTest;

    @Override
    protected void onCreate(Bundle savedInstanceState){
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_second);
        setTitle("Second Activity");

        btnBack = (Button) findViewById(R.id.btnBack);
        textViewTest = (TextView) findViewById(R.id.textViewTest);

        textViewTest.setText(getIntent().getStringExtra("data"));

        btnBack.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                finish();
            }
        });
    }
}
