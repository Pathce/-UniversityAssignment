package com.example.imageview_soundpoolexample;

import androidx.appcompat.app.AppCompatActivity;

import android.media.SoundPool;
import android.net.Uri;
import android.os.Bundle;
import android.view.View;
import android.widget.ImageButton;
import android.widget.ImageView;

import java.util.HashMap;

public class MainActivity extends AppCompatActivity {
    private ImageView imageView;
    private ImageButton imageButton;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        imageView = (ImageView) findViewById(R.id.imageView);
        imageButton = (ImageButton) findViewById(R.id.imageButton);

        MySoundPlayer.initSounds(getApplicationContext());

        imageView.setOnClickListener((v -> {
            MySoundPlayer.play(MySoundPlayer.SUCCESS);
        }));

        imageButton.setOnClickListener((v -> {
            MySoundPlayer.play(MySoundPlayer.DING_DONG);
        }));
    }
}