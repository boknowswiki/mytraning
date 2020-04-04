package main

import (
	"bufio"
	"encoding/json"
	"fmt"
	"net"
)

type response1 struct {
	Page   int
	Fruits []string
}

type response2 struct {
	Page   int      `json:"page"`
	Fruits []string `json:"fruits"`
}

type client struct {
	name string
	val  []byte
}

type clientBool struct {
	Name string
	Val  []byte
}

func testBool() {
	fmt.Println("test bool type:")
	var testType bool
	testType = true
	bolB, _ := json.Marshal(testType)

	c := client{
		"cfg.test",
		bolB,
	}

	fmt.Println(c)
	testType = false

	json.Unmarshal(bolB, &testType)
	fmt.Println(testType)
	fmt.Printf("type is %T\n", testType)

	fmt.Println("json the client:")
	cb := &clientBool{
		Name: "cfg.test_bool",
		Val:  bolB,
	}
	fmt.Println(cb, cb.Name, cb.Val)
	jc, _ := json.Marshal(cb)
	fmt.Println(jc, string(jc))

	var ujc clientBool

	json.Unmarshal(jc, &ujc)
	fmt.Println(ujc)
	var valB bool
	json.Unmarshal(ujc.Val, &valB)
	fmt.Println("valB ", valB)
}

func testInt() {
	fmt.Println("test int type:")
	var testType int
	testType = 123
	intB, _ := json.Marshal(testType)

	c := client{
		name: "cfg.test",
		val:  intB,
	}

	fmt.Println(c)
	testType = 0

	json.Unmarshal(intB, &testType)
	fmt.Println(testType)
	fmt.Printf("type is %T\n", testType)
}

func testFloat() {
	fmt.Println("test float type:")
	var testType float64
	testType = 1.23
	fltB, _ := json.Marshal(testType)

	c := client{
		name: "cfg.test",
		val:  fltB,
	}

	fmt.Println(c)
	testType = 0

	json.Unmarshal(fltB, &testType)
	fmt.Println(testType)
	fmt.Printf("type is %T\n", testType)
}

func testStr() {
	fmt.Println("test string type:")
	var testType string
	testType = "test.test"
	strB, _ := json.Marshal(testType)

	c := client{
		name: "cfg.test",
		val:  strB,
	}

	fmt.Println(c)
	testType = "123"

	json.Unmarshal(strB, &testType)
	fmt.Println(testType)
	fmt.Printf("type is %T\n", testType)
}

func testSlc() {
	fmt.Println("test slice type:")
	testType := []string{"abc", "def", "ghi", "...", "xyz"}
	//testType = "test.test"
	slcB, _ := json.Marshal(testType)

	c := client{
		name: "cfg.test",
		val:  slcB,
	}

	fmt.Println(c)
	testType[0] = "test"

	fmt.Println(testType, string(slcB))
	json.Unmarshal(slcB, &testType)
	fmt.Println(testType)
	fmt.Printf("type is %T\n", testType)
}

func testMap() {
	fmt.Println("test map type:")
	testType := map[string]int{"key1": 1, "key2": 2}
	//testType = "test.test"
	mapB, _ := json.Marshal(testType)

	c := client{
		name: "cfg.test",
		val:  mapB,
	}

	fmt.Println(c)
	testType["key1"] = 3

	fmt.Println(testType, string(mapB))
	json.Unmarshal(mapB, &testType)
	fmt.Println(testType)
	fmt.Printf("type is %T\n", testType)
}

func testNestMap() {
	fmt.Println("test nest map type: ")
	nestMapB := []byte(`{"name": "test", "cnt": 3, "list":["l1", "l2"], 
						"nestKey": {"key1": "val1", "key2": 2}}`)
	var nestMap map[string]interface{}

	err := json.Unmarshal(nestMapB, &nestMap)
	if err != nil {
		panic(err)
	}
	fmt.Println(nestMap)
	fmt.Println(nestMap["name"].(string), nestMap["cnt"].(float64),
		nestMap["list"].([]interface{})[0].(string),
		nestMap["list"].([]interface{})[1].(string),
		nestMap["nestKey"].(map[string]interface{})["key1"].(string),
		nestMap["nestKey"].(map[string]interface{})["key2"].(float64))
}

func test() {

	/*
		testBool()

		testInt()

		testFloat()

		testStr()

		testSlc()

		testMap()

		testNestMap()
		fmt.Println("end of test")
	*/

}

type clientAPI struct {
	Target   string
	Req_type string
	Tx_id    string
	Node     string
	Data     string
	Status   int
}

func checkErr(err error) {
	if err != nil {
		panic(err)
	}
}

func main() {
	fmt.Println("connecting to server...")

	conn, err := net.Dial("tcp", "127.0.0.1:28880")
	checkErr(err)

	defer conn.Close()

	c := clientAPI{
		"sysd",
		"read",
		"99",
		"cfg.test",
		"test",
		0,
	}

	fmt.Println(c)
	out, err := json.Marshal(c)
	checkErr(err)

	out = append(out, "\n"...)
	fmt.Println("sending out ", out)
	conn.Write(out)

	r := bufio.NewReader(conn)
	fmt.Println("waiting for read")
	deli := '\n'
	line, err := r.ReadBytes(byte(deli))

	//line, _, err := r.ReadLine()

	fmt.Println("got ", line)
	fmt.Println(string(line))

	var res resp

	json.Unmarshal(line, &res)

	fmt.Println(res)
	fmt.Println(res.Data)
	//var resMap map[string]interface{}
	//err = json.Unmarshal([]byte(res.Data), &resMap)
	//checkErr(err)
	//fmt.Println(resMap)

	/*
		buf := make([]byte, 1024)
		_, err = conn.Read(buf)
		checkErr(err)
		fmt.Println("got ", buf, string(buf))
		json.Unmarshal(buf, &c)
		fmt.Println(c)
	*/

	nClient := newClient()

	fmt.Println(nClient)

	goObj := GoObj{
		"sysd",
		"read",
		"99",
		"cfg.test",
		"test",
		0,
	}

	fmt.Println(goObj)
	nClient.modify()
	res = nClient.fetch(goObj)

	fmt.Println(res)
}
