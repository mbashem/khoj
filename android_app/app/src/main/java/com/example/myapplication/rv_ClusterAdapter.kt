package com.example.android_practice

import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.TextView
import androidx.recyclerview.widget.RecyclerView
import com.example.myapplication.R


/* Some of the code is taken from https://github.com/codepath/android_guides/wiki/Using-the-RecyclerView
   This class contains the logic for the RecyclerView for displaying clusters */

class rv_ClusterAdapter(val datalist : MutableList<Cluster>) : RecyclerView.Adapter<rv_ClusterAdapter.ViewHolder>() {

    class ViewHolder(itemview : View) : RecyclerView.ViewHolder(itemview){
        val clusterName = itemview.findViewById<TextView>(R.id.Cluster_Name)
        val clusterStrat = itemview.findViewById<TextView>(R.id.Cluster_Strategy)
    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): ViewHolder {
        val inflater = LayoutInflater.from(parent.context)
        return ViewHolder(inflater.inflate(R.layout.cluster_rv_layout,parent,false))
    }

    override fun onBindViewHolder(holder: ViewHolder, position: Int) {
        val clusterItem = datalist[position]
        holder.clusterName.setText(clusterItem.name)
        holder.clusterStrat.setText(clusterItem.strats)
    }

    override fun getItemCount(): Int {
        return datalist.size
    }

}