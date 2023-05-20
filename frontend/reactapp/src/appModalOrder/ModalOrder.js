import {Fragment, useState} from "react";
import {Button, Modal, ModalHeader, ModalBody} from "reactstrap";
import OrderForm from "../appOrderForm/OrderForm";

const ModalOrder = (props) => {
    const [visible, setVisible] = useState(false)
    var button = <Button onClick={() => toggle()}>Редагувати</Button>;

    const toggle = () => {
        setVisible(!visible)
    }

    if (props.create) {
        button = (
            <Button
                    color="primary"
                    className="ml-auto"
                    onClick={() => toggle()}
                    style={{ minWidth: '200px' }}>
                Додати замовлення
            </Button>
        )
    }
    return (
        <Fragment>
            {button}
            <Modal isOpen={visible} toggle={toggle}>
                <ModalHeader
                    style={{justifyContent: "center"}}>{props.create ? "Додати Замовлення" : "Редагувати замовлення"}</ModalHeader>
                <ModalBody>
                    <OrderForm
                        order={props.order ? props.order : []}
                        resetState={props.resetState}
                        toggle={toggle}
                        newOrder={props.newOrder}
                    />
                </ModalBody>
            </Modal>
        </Fragment>
    )
}
export default ModalOrder;