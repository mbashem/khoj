package com.example.myapplication

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.widget.Button
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView
import com.example.myapplication.R


class ClusterActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.clusters)


        val cluster_list = mutableListOf<Cluster>()

        cluster_list.add(Cluster("Cluster 1","pdf,docx"))
        cluster_list.add(Cluster("Cluster 2","pdf,nonhtml"))
        cluster_list.add(Cluster("Cluster 3","nonhtml,pdf,docx,txt"))


        val rv_cluster = findViewById<View>(R.id.rvClusterList) as RecyclerView
        rv_cluster.layoutManager = LinearLayoutManager(this)
        rv_cluster.adapter = rv_ClusterAdapter(cluster_list)



    }
}