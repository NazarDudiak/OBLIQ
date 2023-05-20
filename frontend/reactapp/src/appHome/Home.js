import {Container, Row, Col} from "reactstrap";
import ListOrders from "../appListOrders/ListOrders";
import axios from "axios";
import {useEffect, useState} from "react";
import ModalOrder from "../appModalOrder/ModalOrder";
import {API_URL} from "../index";

const Home = () => {
    const [orders, setOrders] = useState([])

    useEffect(()=>{
        setOrders()
    },[])

    const getOrders = (data)=>{
        axios.get(API_URL).then(data => setOrders(data.data))
    }

    const resetState = () => {
        getOrders();
    };

    return (
        <Container style={{marginTop: "20px"}}>
            <Row>
                <Col>
                    <ListOrders orders={orders} resetState={resetState} newOrder={false}/>
                </Col>
            </Row>
            <Row>
                <Col>
                    <ModalOrder
                    create={true}
                    resetState={resetState}
                    newOrder={true}/>
                </Col>
            </Row>
        </Container>
    )
}

export default Home;