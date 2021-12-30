package com.example.myapplication

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.util.Log
import android.view.View
import android.widget.Button
import android.widget.TextView
import androidx.annotation.NonNull
import com.google.android.gms.auth.api.signin.GoogleSignIn
import com.google.android.gms.auth.api.signin.GoogleSignInClient

import com.google.android.gms.tasks.OnCompleteListener
import com.google.android.gms.auth.api.signin.GoogleSignInOptions
import com.google.android.gms.common.SignInButton


class SearchActivity : AppCompatActivity() {

    lateinit var mTextview: TextView
    private lateinit var mGoogleSignInClient : GoogleSignInClient



    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_search)

        val gso = GoogleSignInOptions.Builder(GoogleSignInOptions.DEFAULT_SIGN_IN).build()
        mGoogleSignInClient = GoogleSignIn.getClient(this, gso);

        mTextview = findViewById(R.id.textView2);

        mTextview.setText(getIntent().getStringExtra("username"));

        val account = GoogleSignIn.getLastSignedInAccount(this)
//        updateUI(account)

        if(account != null) {
            Log.e("WTF:", "WTF")
        }

        val signOutButton = findViewById<Button>(R.id.sign_out_button)

        signOutButton.setOnClickListener(object : View.OnClickListener{
            override fun onClick(v: View?) {
                signOut()
            }})
    }

    private fun signOut() {
        mGoogleSignInClient.signOut()
            .addOnCompleteListener(this, OnCompleteListener<Void?> {
                var changePage = Intent(this,MainActivity::class.java)

                startActivity(changePage)
            })
    }
}