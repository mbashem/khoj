package com.example.myapplication

import android.content.Intent
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.Button
import android.widget.TextView
import androidx.core.content.ContextCompat.startActivity
import androidx.recyclerview.widget.RecyclerView
import com.example.myapplication.R


/* Some of the code is taken from https://github.com/codepath/android_guides/wiki/Using-the-RecyclerView
   This class contains the logic for the RecyclerView for displaying clusters */

class rv_ClusterAdapter(val datalist : MutableList<Cluster>) : RecyclerView.Adapter<rv_ClusterAdapter.ViewHolder>() {

    class ViewHolder( val itemview : View) : RecyclerView.ViewHolder(itemview){
        val clusterName = itemview.findViewById<TextView>(R.id.Cluster_Name)
        val clusterStrat = itemview.findViewById<TextView>(R.id.Cluster_Strategy)
    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): ViewHolder {
        val inflater = LayoutInflater.from(parent.context)
        val view = inflater.inflate(R.layout.cluster_rv_layout,parent,false)
        return ViewHolder(view)
    }

    override fun onBindViewHolder(holder: ViewHolder, position: Int) {
        val clusterItem = datalist[position]
        holder.clusterName.setText(clusterItem.name)
        holder.clusterStrat.setText(clusterItem.strats)
        holder.itemview.setOnClickListener() {
            holder.itemview.context.startActivity(Intent(holder.itemview.context,ClusterSearchActivity::class.java)) }

    }

    override fun getItemCount(): Int {
        return datalist.size
    }

}



