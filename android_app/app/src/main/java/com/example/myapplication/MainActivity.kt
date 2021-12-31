package com.example.myapplication

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import com.google.android.gms.auth.api.signin.GoogleSignIn
import com.google.android.gms.auth.api.signin.GoogleSignInClient
import com.google.android.gms.auth.api.signin.GoogleSignInOptions
import com.google.android.gms.auth.api.signin.GoogleSignInAccount
import com.google.android.gms.common.SignInButton

import android.view.View

import android.content.Intent
import android.net.Uri
import android.util.Log
import android.widget.Toast
import com.github.kittinunf.fuel.Fuel
import com.google.android.gms.common.api.ApiException
import com.google.android.gms.tasks.Task
import com.github.kittinunf.fuel.httpGet
import com.github.kittinunf.fuel.json.jsonDeserializer
import com.github.kittinunf.result.Result;
import org.json.JSONObject

class MainActivity : AppCompatActivity() {
    public lateinit var mGoogleSignInClient: GoogleSignInClient
    private val RC_SIGN_IN = 7

    private val webApplicationClientId =
        "929445193196-i10lnio3bchmjp5bhc1ads8hikrej38s.apps.googleusercontent.com"

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        // Configure sign-in to request the user's ID, email address, and basic
// profile. ID and basic profile are included in DEFAULT_SIGN_IN.
        // Configure sign-in to request the user's ID, email address, and basic
// profile. ID and basic profile are included in DEFAULT_SIGN_IN.
        val gso = GoogleSignInOptions.Builder(GoogleSignInOptions.DEFAULT_SIGN_IN)
            .requestIdToken(getString(R.string.server_client_id))
            .requestEmail()
            .build()

        // Build a GoogleSignInClient with the options specified by gso.
        mGoogleSignInClient = GoogleSignIn.getClient(this, gso);


        // Check for existing Google Sign In account, if the user is already signed in
// the GoogleSignInAccount will be non-null.
        // Check for existing Google Sign In account, if the user is already signed in
// the GoogleSignInAccount will be non-null.
        val account = GoogleSignIn.getLastSignedInAccount(this)
//        updateUI(account)

        if (account != null) {
            Log.e("WTF:", "WTF")
        }

        val signInButton = findViewById<SignInButton>(R.id.sign_in_button)
        signInButton.setSize(SignInButton.SIZE_STANDARD)

        signInButton.setOnClickListener(object : View.OnClickListener {
            override fun onClick(v: View?) {
                signIn()
            }
        })
//        findViewById(R.id.sign_in_button).setOnClickListener(this);
    }

    private fun signIn() {
        val signInIntent = mGoogleSignInClient.signInIntent
        startActivityForResult(signInIntent, RC_SIGN_IN)
    }

    override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) {
        super.onActivityResult(requestCode, resultCode, data)

        // Result returned from launching the Intent from GoogleSignInClient.getSignInIntent(...);
        if (requestCode == RC_SIGN_IN) {
            // The Task returned from this call is always completed, no need to attach
            // a listener.
            val task: Task<GoogleSignInAccount> = GoogleSignIn.getSignedInAccountFromIntent(data)
            handleSignInResult(task)
        }
    }

    private fun handleSignInResult(completedTask: Task<GoogleSignInAccount>) {
        try {
            val account: GoogleSignInAccount = completedTask.getResult(ApiException::class.java)
            val acct = GoogleSignIn.getLastSignedInAccount(this)
            if (acct != null) {
                val personName = acct.displayName
                val personGivenName = acct.givenName
                val personFamilyName = acct.familyName
                val personEmail = acct.email
                val personId = acct.id
                val personPhoto: Uri = acct.photoUrl
                val idToken = acct.idToken;

                val site_url = "http://10.0.2.2:8000/API/verify_user/?id_token=" + idToken

                Log.d("url", site_url)

                Fuel.get(site_url)
                    .response { request, response, result ->
                        when (result) {
                            is Result.Failure -> {
                                mGoogleSignInClient.signOut()
                                val ex = result.getException()
                                println(ex)
                                Toast.makeText(
                                    this,
                                    "Error. Note: Only sign in allowed",
                                    Toast.LENGTH_SHORT
                                ).show()

                            }
                            is Result.Success -> {

                                val data = result.get()
                                println(data)
                                val myBody = String(response.data)
                                val status = JSONObject(String(response.data)).getString("status")
                                if (status == "OK") {
                                    val username =
                                        JSONObject(String(response.data)).getString("username")

                                    Log.d("response", myBody)
                                    Log.d("Token:", idToken)

                                    println(response.body().toString())

                                    Toast.makeText(
                                        this,
                                        "User email: " + personEmail,
                                        Toast.LENGTH_SHORT
                                    ).show()

                                    var changePage = Intent(this, SearchActivity::class.java)

                                    changePage.putExtra("username", username)
                                    changePage.putExtra("token", idToken)

                                    startActivity(changePage)
                                } else {
                                    mGoogleSignInClient.signOut()
                                    Toast.makeText(
                                        this,
                                        "Error. Note: Only sign in allowed",
                                        Toast.LENGTH_SHORT
                                    ).show()
                                }
                            }
                        }
                    }


            }
            // Signed in successfully, show authenticated UI.
        } catch (e: ApiException) {
            // The ApiException status code indicates the detailed failure reason.
            // Please refer to the GoogleSignInStatusCodes class reference for more information.
            Log.e("Message", e.toString())
        }
    }
}