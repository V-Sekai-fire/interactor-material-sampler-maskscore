import QtQuick
import QtQuick.Controls
import MaterialSamplerMaskScore

import Panels
import Spectrum.Controls
import Widgets

PanelBase {
    id: root

    MaterialSamplerMaskScore {
        id: api
    }

    PanelContent {
        Column {
            width: parent.width
            spacing: 20

            TextField {
                id: imagePath
                width: parent.width
                placeholderText: "Path to a garment photograph"
            }

            Button {
                text: "Build material"
                size: Button.Size.Medium
                anchors.horizontalCenter: parent.horizontalCenter
                onClicked: () => api.build_material(imagePath.text)
            }
        }
    }
}
