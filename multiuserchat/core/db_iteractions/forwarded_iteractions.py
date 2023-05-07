from typing import List, Any, Tuple

from multiuserchat.db_models import engine
from multiuserchat.db_models.models import ForwardedMessages
from sqlalchemy.orm import Session


class ForwardedMessageInterface:  # TODO If the message is deleted, then its row should be deleted from this table

    @staticmethod
    def get_conv_forwarded_all_msg(conv_id: int) -> List:  # TODO whether this method should return tuple of (forward, origin) msg ids or Session method
        with Session(bind=engine) as session:
            conv_data = session.query(ForwardedMessages).filter(ForwardedMessages.conversation_id == conv_id).all()
        return [(obj.origin_id, obj.forward_id, obj.timestamp) for obj in conv_data]

    @staticmethod
    def from_forward_get_origin_with_conv(forward_id: int) -> Tuple[Any, Any]:
        with Session(bind=engine) as session:
            forward_msg = session.query(ForwardedMessages).filter(ForwardedMessages.forward_id == forward_id).one_or_none()
        return forward_msg.origin_id, forward_msg.conversation_id
