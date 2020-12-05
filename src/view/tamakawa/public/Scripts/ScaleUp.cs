using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ScaleUp : MonoBehaviour
{
    public float dx = 2;
    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        if
            this.transform.localScale += new Vector3(0.0001f, 0.001f, 0);
        //this.transform.localScale = new Vector3( (Time.deltaTime + 1) ,  (Time.deltaTime +1 ), 1);
        //for(int i = 0;i < 10;i++){
            //this.transform.localScale = new Vector3(1.000002f, 1.0005f, 1);
        //}
    }
}
