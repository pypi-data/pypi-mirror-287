from torch.utils.data import DataLoader

from scripts.dataset import get_heart_train_dataset


def main():
    print('position0')
    train_dataset = get_heart_train_dataset()
    print('position1')
    train_dataloader = DataLoader(
        train_dataset,
        batch_size=1000,
        persistent_workers=True,
        prefetch_factor=10,
        num_workers=5,
    )
    print('position2')
    for batch_index, batch in enumerate(train_dataloader):
        if batch_index % 100 == 0:
            print(batch_index, flush=True)


if __name__ == '__main__':
    main()
