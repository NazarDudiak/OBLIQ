import {useEffect, useState} from "react";
import {Button, Form, FormGroup, Input, Label} from "reactstrap";
import axios from "axios";
import {API_URL} from "../index";

const OrderForm = (props) => {
    const [order, setOrder] = useState({})

    const onChange = (e) => {
        const newState = order
        if (e.target.name === "photo") {
            console.log(e.target.files[0])
            newState[e.target.name] = e.target.files[0]
        } else newState[e.target.name] = e.target.value
        setOrder(newState)
    }

    useEffect(() => {
        if (!props.newOrder) {
            setOrder(Order => props.order)
        }
        // eslint-disable-next-line
    }, [props.order])


    const defaultIfEmpty = value => {
        return value === "" ? "" : value;
    }

    const submitDataEdit = async (e) => {
        e.preventDefault();
        // eslint-disable-next-line
        const result = await axios.put(API_URL + order.id + "/", order, {headers: {'Content-Type': 'multipart/form-data'}})
            .then(() => {
                props.resetState()
                props.toggle()
            })
    }
    const submitDataAdd = async (e) => {
        e.preventDefault();
        const formData = new FormData();
        formData.append("name", order.name);
        formData.append("email", order.email);
        formData.append("address", order.address);
        formData.append("phone", order.phone);
        formData.append("photo", order.photo);
    
        try {
            await axios.post(API_URL, formData, {
            headers: {
                "Content-Type": "multipart/form-data",
            },
        });
        props.resetState();
        props.toggle();
        } catch (error) {
          // Обробка помилки
        }
    };
    
    return (
        <Form onSubmit={props.newOrder ? submitDataAdd : submitDataEdit}>
            <FormGroup>
                <Label for="name">Name:</Label>
                <Input
                    type="text"
                    name="name"
                    onChange={onChange}
                    defaultValue={defaultIfEmpty(order.name)}
                />
            </FormGroup>
            <FormGroup>
                <Label for="email">Email</Label>
                <Input
                    type="email"
                    name="email"
                    onChange={onChange}
                    defaultValue={defaultIfEmpty(order.email)}
                />
            </FormGroup>
            <FormGroup>
                <Label for="address">Address:</Label>
                <Input
                    type="text"
                    name="address"
                    onChange={onChange}
                    defaultValue={defaultIfEmpty(order.address)}
                />
            </FormGroup>
            <FormGroup>
                <Label for="phone">Phone:</Label>
                <Input
                    type="text"
                    name="phone"
                    onChange={onChange}
                    defaultValue={defaultIfEmpty(order.phone)}
                />
            </FormGroup>
            <FormGroup>
                <Label for="photo">Photo:</Label>
                <Input
                    type="file"
                    name="photo"
                    onChange={onChange}
                    accept='image/*'
                />
            </FormGroup>
            <div style={{display: "flex", justifyContent: "space-between"}}>
                <Button>Send</Button> <Button onClick={props.toggle}>Cancel</Button>
            </div>
        </Form>
    )
}

export default OrderForm;