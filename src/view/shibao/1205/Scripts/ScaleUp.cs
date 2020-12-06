using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ScaleUp : MonoBehaviour
{
    public float dx = 2;
    public float vec = 1;
    
    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {   

        //this.transform.localScale += new Vector3(Mathf.Sin (Time.time) * 0.001f, 0.001f, 0);
        if(vec == 1){
            if(this.transform.localScale.x < 2 && this.transform.localScale.y < 2 ){
                this.transform.localScale += new Vector3(0.001f, 0.001f, 0);
            }
            else if(this.transform.localScale.x >= 1.5){
                //this.transform.lossyScale = new Vector3(1.5f, 1.5f, 1);
                gameObject.SetActive (false);
                vec = 0;
            }
        }
        if(vec == 0){
            if(this.transform.localScale.x > 1 && this.transform.localScale.y > 1 ){
                this.transform.localScale += new Vector3(-0.001f, -0.001f, 0);
        }
        else if(this.transform.localScale.x <= 1 ){//this.transform.localScale.x > 1 && this.transform.localScale.y > 1) {
            Debug.Log("Bigger!!");
            //this.transform.lossyScale = new Vector3(1, 1, 1);
            vec = 1;
        }

        }
       
        
        //this.transform.localScale = new Vector3( (Time.deltaTime + 1) ,  (Time.deltaTime +1 ), 1);
        //for(int i = 0;i < 10;i++){
            //this.transform.localScale = new Vector3(1.000002f, 1.0005f, 1);
        //}
    }
}
