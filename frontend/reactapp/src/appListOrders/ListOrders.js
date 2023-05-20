import {Table} from "reactstrap";
import ModalOrder from "../appModalOrder/ModalOrder";
import AppRemoveOrder from "../appRemoveOrder/appRemoveOrder";
import ModalPhoto from "../appPhotoModal/ModalPhoto";

const ListOrders = (props) => {
    // debugger
    const {orders} = props
    return (
        <Table dark>
            <thead>
            <tr>
                <th>ПІБ</th>
                <th>Email</th>
                <th>Адреса</th>
                <th>Телефон</th>
                <th>Дата створення</th>
                <th>Фото</th>
                <th></th>
            </tr>
            </thead>
            <tbody>
            {!orders || orders.length <= 0 ? (
                <tr>
                    <td colSpan="7" align="center">
                        <b>Поки замовлень немає</b>
                    </td>
                </tr>
            ) : orders.map(order => (
                    <tr key={order.id}>
                        <td className="align-middle">{order.name}</td>
                        <td className="align-middle">{order.email}</td>
                        <td className="align-middle">{order.address}</td>
                        <td className="align-middle">{order.phone}</td>
                        <td className="align-middle">{order.registrationDate}</td>
                        <td className="align-middle"><ModalPhoto order={order}/></td>
                        <td style={{ width: '18%' }} className="align-middle">
                        <ModalOrder
                                create={false}
                                order={order}
                                resetState={props.resetState}
                                newOrder={props.newOrder}
                            />
                            &nbsp;&nbsp;
                            <AppRemoveOrder
                                id={order.id}
                                resetState={props.resetState}
                            />
                        </td>
                    </tr>
                )
            )}
            </tbody>
        </Table>
    )
}
export default ListOrders