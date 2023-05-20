import {Fragment, useState} from "react";
import {Button, Modal, ModalHeader, ModalFooter} from "reactstrap";
import axios from "axios";
import {API_URL} from "../index";

const AppRemoveOrder = (props) => {
    const [visible, setVisible] = useState(false)
    const toggle = () => {
        setVisible(!visible)
    }
    const deleteOrder = () => {
        axios.delete(API_URL + props.id + "/").then(() => {
            props.resetState()
            toggle();
        });
    }
    return (
        <Fragment>
            <Button color="danger" onClick={() => toggle()}>
                Видалити
            </Button>
            <Modal isOpen={visible} toggle={toggle} style={{width: "300px"}}>
                <ModalHeader style={{justifyContent: "center"}}>Ви впевнені?</ModalHeader>
                <ModalFooter style={{display: "flex", justifyContent: "space-between"}}>
                    <Button
                        type="button"
                        onClick={() => deleteOrder()}
                        color="primary"
                    >Видалити</Button>
                    <Button type="button" onClick={() => toggle()}>Відміна</Button>
                </ModalFooter>
            </Modal>
        </Fragment>
    )
}
export default AppRemoveOrder;