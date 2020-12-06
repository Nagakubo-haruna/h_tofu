using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class NewBehaviourScript : MonoBehaviour
{
    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        Vector3 pos = this.gameObject.transform.position;
		this.gameObject.transform.position = new Vector3 (Mathf.Sin (Time.time) * 2.0f, pos.y, pos.z);	
    }
}
